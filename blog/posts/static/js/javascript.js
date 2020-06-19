// Função para envio de imagem na postagem
var $input    = document.getElementById('image')
var $fileName = document.getElementById('file-name')

$input.addEventListener('change', function(){
  $fileName.textContent = this.value;
});
