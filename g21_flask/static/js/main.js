// Esperar que a página carregue completamente
document.addEventListener("DOMContentLoaded", function() {
    
    // Agarrar o botão pelo ID
    let botaoGrafico = document.getElementById("btn-grafico");

    if (botaoGrafico) {
        botaoGrafico.addEventListener("click", function() {
            // Efeito fixe: muda o texto do botão quando clicas
            botaoGrafico.innerHTML = "Loading data... ⏳";
            botaoGrafico.style.transform = "scale(0.95)";
            
            // Espera meio segundo (para se ver a animação) e redireciona para o gráfico
            setTimeout(function() {
                window.location.href = "/ranking-exposicoes";
            }, 500);
        });
    }
});