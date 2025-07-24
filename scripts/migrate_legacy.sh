#!/usr/bin/env bash
set -euo pipefail

# 1. Ask for defaults
read -p "Default author for legacy notes? [Rick] " DEFAULT_AUTHOR
DEFAULT_AUTHOR=${DEFAULT_AUTHOR:-Rick}

read -p "Default type for legacy notes? [SQLConversion] " DEFAULT_TYPE
DEFAULT_TYPE=${DEFAULT_TYPE:-SQLConversion}

# 2. Clean up old artifacts
echo "🧹 Removing legacy artifacts..."
rm -rf .archive
rm -f generate_prompt.py mcp.config.json

# 3. Ensure our target notes directory exists
echo "📁 Preparing notes/Validator directory..."
mkdir -p notes/Validator

# 4. Move legacy fixtures into notes/Validator
if [[ -d notes/validator/fixtures ]]; then
  echo "🚚 Moving legacy fixtures..."
  mv notes/validator/fixtures/* notes/Validator/
  rm -rf notes/validator
fi

# 5. Convert each legacy file into a Markdown note
echo "✍️  Converting legacy files to Markdown notes..."
idx=1
for legacy in notes/Validator/*; do
  ext="${legacy##*.}"
  base="$(basename "$legacy" ".$ext")"
  # Create a PascalCase slug from the basename
  slug="$(echo "$base" | sed -E 's/[^a-zA-Z0-9]/ /g' | \
         awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)}1' | tr -d ' ')"
  # Zero‑padded order prefix
  prefix=$(printf "%02d" $idx)
  outfile="notes/Validator/${prefix}_${slug}.md"

  cat > "$outfile" <<EOF
---
title: $slug
slug: $slug
author: $DEFAULT_AUTHOR
type: $DEFAULT_TYPE
tags: [$slug]
level: Atomic
---

\`\`\`$ext
$(<"$legacy")
\`\`\`
EOF

  echo " • Converted $legacy → $outfile"
  ((idx++))
done

# 6. Update notes.config.json with the new ordering
echo "🔢 Regenerating notes.config.json..."
jq -n --argfile files <(ls notes/Validator/*.md | sort) \
    '{ order: ($files | map(split("/") | .[-1])) }' \
    > notes.config.json

echo "✅ Migration complete!"
echo "Review notes/Validator/*.md to tweak frontmatter as needed."
