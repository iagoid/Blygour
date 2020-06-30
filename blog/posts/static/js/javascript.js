// Função para pegar o nome da imagem
var $input    = document.getElementById('input-file')
var $fileName = document.getElementById('file-name')

$input.addEventListener('change', function(){
  $fileName.textContent = this.value;
});
