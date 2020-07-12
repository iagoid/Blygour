// Função para pegar o nome da imagem
var $input    = document.getElementById('input-file')
var $fileName = document.getElementById('file-name')

$input.addEventListener('change', function(){
  $fileName.textContent = this.value;
});


// Função para ocultar o campo de respostas

function AparecerResposta(id){
  document.getElementById(id).hidden = false
}