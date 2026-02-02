const makeSlug = (str) => {
  const from = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я ā ą ä á à â å č ć ē ę ě é è ê æ ģ ğ ö ó ø ǿ ô ő ḿ ŉ ń ṕ ŕ ş ü ß ř ł đ þ ĥ ḧ ī ï í î ĵ ķ ł ņ ń ň ř š ś ť ů ú û ứ ù ü ű ū ý ÿ ž ź ż ç є ґ".split(' ');
  const to = "a b v g d e e zh z i y k l m n o p r s t u f h ts ch sh shch # y # e yu ya a a ae a a a a c c e e e e e e e g g oe o o o o o m n n p r s ue ss r l d th h h i i i i j k l n n n r s s t u u u u u u u u y y z z z c ye g".split(' ');

  str = str.toLowerCase();

  // remove simple HTML tags
  str = str.replace(/(<[a-z0-9\-]{1,15}[\s]*>)/gi, '');
  str = str.replace(/(<\/[a-z0-9\-]{1,15}[\s]*>)/gi, '');
  str = str.replace(/(<[a-z0-9\-]{1,15}[\s]*\/>)/gi, '');

  str = str.replace(/^\s+|\s+$/gm, ''); // trim spaces

  for (let i = 0; i < from.length; ++i)
    str = str.split(from[i]).join(to[i]);

  // Replace different kind of spaces with dashes
  let spaces = [/(&nbsp;|&#160;|&#32;)/gi, /(&mdash;|&ndash;|&#8209;)/gi,
    /[(_|=|\\|\,|\.|!)]+/gi, /\s/gi];

  for (let i = 0; i < from.length; ++i)
    str = str.replace(spaces[i], '-');
  str = str.replace(/-{2,}/g, "-");

  // remove special chars like &amp;
  str = str.replace(/&[a-z]{2,7};/gi, '');
  str = str.replace(/&#[0-9]{1,6};/gi, '');
  str = str.replace(/&#x[0-9a-f]{1,6};/gi, '');

  str = str.replace(/[^a-z0-9\-]+/gmi, ""); // remove all other stuff
  str = str.replace(/^\-+|\-+$/gm, ''); // trim edges

  return str;
};

const nameField = document.getElementById("id_name");

nameField?.addEventListener("keyup", (e) => {
  const isEditPage = window.location.pathname.includes('/edit/');
  if(!isEditPage){
    document.getElementById("id_slug").value = makeSlug(e.target.value);
  }
})
