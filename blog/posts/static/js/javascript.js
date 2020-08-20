// Tempo que mensagens aparecem na tela
$(document).ready(function() {
  // messages timeout for 5 sec 
  setTimeout(function() {
      $('.messages').fadeOut('slow');
  }, 5000); // <-- time in milliseconds, 1000 =  1 sec
});

// Função para pegar o nome da imagem
function postarImagem() {
  var $input = document.getElementById('input-file')
  var $fileName = document.getElementById('file-name')

  $input.addEventListener('change', function () {
    $fileName.textContent = this.value;
  });
};

// TODO: colocar imagem em um local adequado
// $(function(){
//   $('#input-file').change(function(){
//     const file = $(this)[0].files[0]
//     const fileReader = new FileReader()
//     fileReader.onloadend = function(){
//       $('#img').attr('src', fileReader.result)
//     }
//     fileReader.readAsDataURL(file)
//   })
// })


// Exibir e ocultar respostas de comentários
$(".comment-reply-btn").click(function () {
  $(this).parent().next(".comment-reply").fadeToggle();
});



