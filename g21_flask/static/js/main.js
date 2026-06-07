
document.addEventListener("DOMContentLoaded", function() {
    

    let botaoGrafico = document.getElementById("btn-grafico");

    if (botaoGrafico) {
        botaoGrafico.addEventListener("click", function() {

            botaoGrafico.innerHTML = "Loading data... ⏳";
            botaoGrafico.style.transform = "scale(0.95)";
            

            setTimeout(function() {
                window.location.href = "/ranking-exposicoes";
            }, 500);
        });
    }
});
