// Função para pegar o nome da imagem
function postarImagem() {
  var $input = document.getElementById('input-file')
  var $fileName = document.getElementById('file-name')

  $input.addEventListener('change', function () {
    $fileName.textContent = this.value;
  });
}

$(".comment-reply-btn").click(function () {
  $(this).parent().next(".comment-reply").fadeToggle();
});

$(".see-reply-btn").click(function () {
  $(this).parent().next(".see-reply").fadeToggle();
});

