// ── Componente: Modal de Créditos ────────────────────────────

// 1. CSS
const style = document.createElement('style');
style.textContent = `
  #credits-btn {
    background: none;
    border: none;
    color: inherit;
    font: inherit;
    cursor: pointer;
    padding: 0;
    opacity: 0.5;
    transition: opacity 0.2s;
  }
  #credits-btn:hover { opacity: 1; }

  .credits-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(3px);
  }
  .credits-overlay.open { display: flex; }

  .credits-box {
    background: #fdfcfa;
    border-radius: 12px;
    padding: 2rem 2.2rem;
    max-width: 420px;
    width: 90%;
    position: relative;
    box-shadow: 0 24px 60px rgba(0,0,0,0.18);
    animation: credits-in 0.25s ease;
  }
  @keyframes credits-in {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .credits-box h3 {
    font-family: 'Libre Baskerville', serif;
    font-size: 1.15rem;
    color: #1c1c1c;
    margin-bottom: 10px;
  }
  .credits-divider {
    display: flex;
    gap: 4px;
    margin-bottom: 20px;
  }
  .credits-divider span {
    height: 4px;
    width: 28px;
    border-radius: 2px;
    display: block;
  }
  .credits-divider span:nth-child(1) { background: #c0392b; }
  .credits-divider span:nth-child(2) { background: #d4a017; }
  .credits-divider span:nth-child(3) { background: #1a5276; }
  .credits-box ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .credits-box ul li {
    padding: 8px 0;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    font-size: 0.88rem;
    color: #6b6560;
    line-height: 1.5;
  }
  .credits-box ul li:last-child { border-bottom: none; }
  .credits-box ul li strong { color: #1c1c1c; }

  #credits-close {
    position: absolute;
    top: 0.9rem; right: 0.9rem;
    background: none;
    border: none;
    font-size: 0.95rem;
    cursor: pointer;
    color: #6b6560;
    padding: 4px;
    border-radius: 4px;
    transition: color 0.2s, background 0.2s;
  }
  #credits-close:hover { color: #1c1c1c; background: rgba(0,0,0,0.06); }
`;
document.head.appendChild(style);

// 2. HTML del modal
const modal = document.createElement('div');
modal.id = 'credits-modal';
modal.className = 'credits-overlay';
modal.innerHTML = `
  <div class="credits-box">
    <button id="credits-close">✕</button>
    <h3>Créditos</h3>
    <div class="credits-divider"><span></span><span></span><span></span></div>
    <ul>
      <li><strong>Dra. Dora Virginia Chávez Corral</strong> — Fundadora y directora del museo</li>
      <!-- NOMBRES DE CONTRIBUYENTES.-->
      <li>Andrés Manuel Andazola González — Programador principal</li>
    </ul>
  </div>
`;
document.body.appendChild(modal);

// 3. Lógica
const creditsBtn   = document.getElementById('credits-btn');
const creditsModal = document.getElementById('credits-modal');
const creditsClose = document.getElementById('credits-close');

creditsBtn.addEventListener('click',  () => creditsModal.classList.add('open'));
creditsClose.addEventListener('click',() => creditsModal.classList.remove('open'));
creditsModal.addEventListener('click', e => {
  if (e.target === creditsModal) creditsModal.classList.remove('open');
});