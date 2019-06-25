// $(document).ready(function(){
//   $('button').click(function(){
//     $('h1').hide();
//   });
// });
//forma reduzida
// $(function(){
//   $('button').click(function(){
//     //$('h1').hide();
//     $('#unico').css("color", "red");
//   });
// });

$(function(){
  // $('#azul').click(function(){
  //   $('p').css("color", "blue");
  //   $('p').fadeOut(); //some devagar
  //   $('p').delay(3000);
  //   $('p').fadeIn();
  // });
  // $('#vermelho').click(function(){
  //    $('p').css("color", "red")
  //    $('#mensagem').text("Cor alterada com sucesso")
  //       .css('color', 'red')
  //       .css('border', '1px solid red')
  //       .delay(3000)
  //       .fadeOut('fast')
  //       .addClass('green')
  //
  //     $('button').removeClass('red');
  //   // $('p').fadeOut('slow'); //some devagar
  //   // $('p').delay(3000);
  //   // $('p').fadeIn('slow'); // fast em ves de slow para ser rápido
  //   // $('#mensagem').text("Cor alterada com sucesso");
  //   // $('#mensagem').css('color', 'red');
  //   // $('#mensagem').css('border', '1px solid red');
  //   //
  //   // $('#mensagem').delay(3000);
  //   // $('#mensagem').fadeOut('fast');
  //
  // });
  $('#l2').click(function(){
    $('#i1').hide();
    $('#i3').hide();
    $('#i2').show();
  });
  $('#l3').click(function(){
    $('#i1').hide();
    $('#i2').hide();
    $('#i3').show();
  });
  $('#l1').click(function(){
    $('#i2').hide();
    $('#i3').hide();
    $('#i1').show();
  });
});
