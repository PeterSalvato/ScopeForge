<?php
$title = "Static Example";
ob_start();
?>
<p>Deterministic content only.</p>
<?php
$content = ob_get_clean();
