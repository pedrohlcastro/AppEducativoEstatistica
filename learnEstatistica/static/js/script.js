var tamanho = $(window).height();
var min = tamanho - $("footer").height();
$(".content").css('min-height',min + 'px');

$( window ).resize(function() {
	var tamanho = $(window).height();
	var min = tamanho - $("footer").height();
	$(".content").css('min-height',min + 'px');
});