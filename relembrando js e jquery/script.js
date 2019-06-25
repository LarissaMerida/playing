// var mensagem = "Ola mundo!"
// alert(mensagem)
// var a = 2
// var b = 3
// var c  = "Ola mundo"
//
// var soma = a+b
// var sub = a-b
// var mult= a*b
// var div = a/b
//
// if (c%2 == 1){
//   alert("Número impar")
// }
// else if (c%2 == 0){
//   alert("Número par")
// }
// else{
//   alert("Valor inválido")
// }

// var i = 0;
//
// while (i < 3){
//   alert(i);
//
//   i += 1;
// }
//
// for( var j = 0; j < 3; j++){
//   alert(j);
// }

// var numero = 6;
// var decimal= 4.5;
// var an = "Ola mundo";
// var lista = ["laranja", "organ", "maca", "aaaa"];
//
// for(i in lista){
//   alert(lista[i]);
// }

// function soma(a, b){
//   console.log(a+b);
// }
//
// soma(2, 2);
//
// function subtracao(a, b){
//   return a-b;
// }
//
// var s = subtracao(5, 3);
// console.log(s);
//
// function multiplicacao(a, b){
//   return a*b;
// }
//
// console.log(multiplicacao(5, 5));

// function mensagem(nome){
//   alert("Clicouuu :C Eiii, não clique em mim, " + nome);
// }
//
// function mensagemOut(nome){
//   alert("Eiii,volte aqui, " + nome);
// }

// function mudaCor(cor){
//   var elemento = document.getElementById("mensagem");
//   //console.log(elemento);
//
// //  elemento.style.color = cor;
// //  elemento.style.backgroundColor = cor;
// }

function valida(){
  var nome = document.getElementById("nome");

  alert(nome.value);

  if( nome.value == ""){
    alert("Campo nome não pode estar em branco.");
  }else{
    alert("Nenhum problema foi detectado. Seu formulário pode ser enviado com sucesso.");
  }
}
