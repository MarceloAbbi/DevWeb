function limpar(){
    document.meu_form.minha_tela.value = "";
}
function inserir(meu_numero){
    document.meu_form.minha_tela.value = document.meu_form.minha_tela.value + meu_numero;  
} 
function deletar(){
    var meu_conteudo = document.meu_form.minha_tela.value;
    document.meu_form.minha_tela.value = meu_conteudo.substring(0 , meu_conteudo.length-1);
}
function total(){
    var meu_resultado = document.meu_form.minha_tela.value;
    if(meu_resultado){
        document.meu_form.minha_tela.value = eval(meu_resultado);
    }
}