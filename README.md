<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Linear Regression Custom — README</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@700;900&display=swap" rel="stylesheet"/>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: #020510;
    color: #e0e8ff;
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
  }

  .grid-bg {
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,255,200,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,255,200,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  /* Floating particles */
  .particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
  .particle {
    position: absolute;
    width: 2px; height: 2px;
    border-radius: 50%;
    animation: float-up linear infinite;
    opacity: 0;
  }
  @keyframes float-up {
    0%   { transform: translateY(100vh) translateX(0); opacity: 0; }
    10%  { opacity: 1; }
    90%  { opacity: 1; }
    100% { transform: translateY(-10vh) translateX(40px); opacity: 0; }
  }

  .content {
    position: relative;
    z-index: 1;
    max-width: 820px;
    margin: 0 auto;
    padding: 56px 28px 80px;
  }

  /* HERO */
  .hero { text-align: center; margin-bottom: 60px; }

  .badge {
    display: inline-block;
    font-size: 11px;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #00ffc8;
    border: 1px solid #00ffc8;
    padding: 5px 16px;
    border-radius: 2px;
    margin-bottom: 24px;
    animation: pulse-border 2.5s ease-in-out infinite;
  }
  @keyframes pulse-border {
    0%,100% { box-shadow: 0 0 6px #00ffc8, inset 0 0 6px rgba(0,255,200,0.1); }
    50%      { box-shadow: 0 0 22px #00ffc8, inset 0 0 14px rgba(0,255,200,0.25); }
  }

  .title {
    font-family: 'Orbitron', sans-serif;
    font-size: 44px;
    font-weight: 900;
    line-height: 1.1;
    background: linear-gradient(135deg, #00ffc8 0%, #7b5fff 50%, #ff4fd8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
    background-size: 200% auto;
    animation: shimmer 4s ease-in-out infinite;
  }
  @keyframes shimmer {
    0%,100% { background-position: 0% center; }
    50%      { background-position: 100% center; }
  }

  .subtitle {
    font-size: 13px;
    color: #7b8ab8;
    letter-spacing: 0.04em;
    max-width: 560px;
    margin: 0 auto;
    line-height: 1.8;
  }

  /* DIVIDER */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #7b5fff, #00ffc8, #ff4fd8, transparent);
    background-size: 200% auto;
    margin: 44px 0;
    animation: flow 3s linear infinite;
  }
  @keyframes flow {
    0%   { background-position: 0% center; }
    100% { background-position: 200% center; }
  }

  /* SECTION */
  .section { margin-bottom: 44px; animation: fade-in 0.6s ease both; }
  @keyframes fade-in {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .section-label {
    font-size: 10px;
    letter-spacing: 0.26em;
    text-transform: uppercase;
    color: #ff4fd8;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #ff4fd8, transparent);
  }

  /* USE CASE BLOCK */
  .use-case-block {
    background: linear-gradient(135deg, rgba(123,95,255,0.08), rgba(0,255,200,0.05));
    border: 1px solid rgba(123,95,255,0.3);
    border-radius: 6px;
    padding: 22px 26px;
    font-size: 14px;
    line-height: 1.9;
    color: #c8d4ff;
  }
  .use-case-block span { color: #00ffc8; font-weight: 700; }

  /* CODE BLOCK */
  .code-block {
    background: #080d1a;
    border: 1px solid rgba(0,255,200,0.15);
    border-left: 3px solid #00ffc8;
    border-radius: 4px;
    padding: 20px 22px;
    font-size: 13px;
    line-height: 2.1;
    color: #7b8ab8;
    position: relative;
    overflow: hidden;
  }
  .code-block::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, #00ffc8, transparent);
  }
  .code-line   { display: block; }
  .code-comment { color: #2e3d5c; }
  .code-cmd    { color: #00ffc8; }
  .code-flag   { color: #ff4fd8; }
  .code-val    { color: #ffd166; }
  .code-pip    { color: #7b5fff; }

  /* TWO COLS */
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

  .info-card {
    background: #080d1a;
    border: 1px solid rgba(123,95,255,0.2);
    border-radius: 6px;
    padding: 20px 22px;
  }
  .info-card-label {
    font-size: 10px;
    letter-spacing: 0.22em;
    color: #7b5fff;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  .info-card-content {
    font-size: 12px;
    color: #8a9bc4;
    line-height: 2;
  }
  .col-tag { color: #00ffc8; }

  /* METRICS */
  .metrics-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 14px; }

  .metric {
    background: #080d1a;
    border: 1px solid rgba(0,255,200,0.1);
    border-radius: 6px;
    padding: 20px 12px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s, border-color 0.3s;
  }
  .metric:hover { transform: translateY(-4px); border-color: rgba(0,255,200,0.45); }
  .metric::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
  }
  .metric.m1::after { background: #00ffc8; box-shadow: 0 0 10px #00ffc8; }
  .metric.m2::after { background: #7b5fff; box-shadow: 0 0 10px #7b5fff; }
  .metric.m3::after { background: #ff4fd8; box-shadow: 0 0 10px #ff4fd8; }
  .metric.m4::after { background: #ffd166; box-shadow: 0 0 10px #ffd166; }

  .metric-name { font-size: 10px; letter-spacing: 0.15em; color: #4a5878; text-transform: uppercase; margin-bottom: 10px; }

  .metric-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 24px;
    font-weight: 700;
    animation: glow-pulse 3s ease-in-out infinite;
  }
  .metric.m1 .metric-val { color: #00ffc8; text-shadow: 0 0 14px rgba(0,255,200,0.7); }
  .metric.m2 .metric-val { color: #7b5fff; text-shadow: 0 0 14px rgba(123,95,255,0.7); }
  .metric.m3 .metric-val { color: #ff4fd8; text-shadow: 0 0 14px rgba(255,79,216,0.7); }
  .metric.m4 .metric-val { color: #ffd166; text-shadow: 0 0 14px rgba(255,209,102,0.7); }

  @keyframes glow-pulse {
    0%,100% { opacity: 1; }
    50%      { opacity: 0.65; }
  }
  .metric-label { font-size: 9px; color: #3d4d72; margin-top: 6px; letter-spacing: 0.1em; }

  /* HOW IT WORKS */
  .steps { display: flex; flex-direction: column; gap: 12px; }
  .step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    background: #080d1a;
    border: 1px solid rgba(123,95,255,0.15);
    border-radius: 6px;
    padding: 16px 20px;
    transition: border-color 0.3s;
  }
  .step:hover { border-color: rgba(123,95,255,0.5); }
  .step-num {
    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: #7b5fff;
    min-width: 28px;
    padding-top: 1px;
  }
  .step-text { font-size: 13px; color: #8a9bc4; line-height: 1.7; }
  .step-text strong { color: #c8d4ff; font-weight: 700; }

  /* PROJECT TREE */
  .tree {
    background: #080d1a;
    border: 1px solid rgba(0,255,200,0.12);
    border-radius: 6px;
    padding: 20px 24px;
    font-size: 13px;
    line-height: 2;
    color: #4a5878;
  }
  .tree .t-dir  { color: #7b5fff; }
  .tree .t-file { color: #00ffc8; }
  .tree .t-main { color: #ff4fd8; }

  /* FOOTER */
  .footer {
    text-align: center;
    margin-top: 60px;
    padding-top: 28px;
    border-top: 1px solid rgba(123,95,255,0.15);
    font-size: 11px;
    color: #2e3a56;
    letter-spacing: 0.12em;
  }
  .footer span { color: #7b5fff; }

  @media (max-width: 620px) {
    .metrics-grid { grid-template-columns: repeat(2,1fr); }
    .cols { grid-template-columns: 1fr; }
    .title { font-size: 28px; }
  }
</style>
</head>
<body>

<div class="grid-bg"></div>

<!-- Particles -->
<div class="particles" id="particles"></div>

<div class="content">

  <!-- HERO -->
  <div class="hero">
    <div class="badge">ML · From Scratch · Gradient Descent</div>
    <div class="title">Linear Regression<br>Custom</div>
    <p class="subtitle">Predicts a student's final exam score out of 100 — built entirely from scratch using Gradient Descent. No sklearn. No shortcuts. Pure Python.</p>
  </div>

  <div class="divider"></div>

  <!-- USE CASE -->
  <div class="section">
    <div class="section-label">Use Case</div>
    <div class="use-case-block">
      Models the relationship between a student's <span>study habits</span> and <span>academic behavior</span> to predict their <span>final exam score</span> — using a Linear Regression engine powered by a custom Gradient Descent optimizer, written entirely from scratch.
    </div>
  </div>

  <!-- SETUP -->
  <div class="section">
    <div class="section-label">Setup</div>
    <div class="code-block">
      <span class="code-line"><span class="code-comment"># Install dependencies</span></span>
      <span class="code-line"><span class="code-pip">pip install</span> <span class="code-val">-r requirements.txt</span></span>
    </div>
  </div>

  <!-- GENERATE DATA -->
  <div class="section">
    <div class="section-label">Generate Sample Data (optional)</div>
    <div class="code-block">
      <span class="code-line"><span class="code-cmd">python</span> <span class="code-val">data_generator.py</span></span>
    </div>
  </div>

  <!-- RUN -->
  <div class="section">
    <div class="section-label">Run the Model</div>
    <div class="code-block">
      <span class="code-line"><span class="code-cmd">python</span> <span class="code-val">main.py</span> \</span>
      <span class="code-line">&nbsp;&nbsp;<span class="code-flag">--data</span> <span class="code-val">data/student_scores.csv</span> \</span>
      <span class="code-line">&nbsp;&nbsp;<span class="code-flag">--target</span> <span class="code-val">final_exam_score</span> \</span>
      <span class="code-line">&nbsp;&nbsp;<span class="code-flag">--epochs</span> <span class="code-val">1000</span> \</span>
      <span class="code-line">&nbsp;&nbsp;<span class="code-flag">--lr</span> <span class="code-val">0.01</span></span>
    </div>
  </div>

  <!-- CSV FORMAT -->
  <div class="section">
    <div class="section-label">CSV Format</div>
    <div class="cols">
      <div class="info-card">
        <div class="info-card-label">Input Features</div>
        <div class="info-card-content">
          <span class="col-tag">study_hours_per_week</span><br>
          <span class="col-tag">attendance_percentage</span><br>
          <span class="col-tag">previous_test_score</span><br>
          <span class="col-tag">assignments_completed</span><br>
          <span class="col-tag">practice_questions_solved</span><br>
          <span class="col-tag">sleep_hours_per_day</span>
        </div>
      </div>
      <div class="info-card">
        <div class="info-card-label">Target Column</div>
        <div class="info-card-content" style="display:flex;flex-direction:column;justify-content:center;height:100%;gap:12px;">
          <div style="color:#4a5878;font-size:11px;letter-spacing:0.1em;">PREDICTS →</div>
          <div style="font-size:20px;color:#00ffc8;font-family:'Orbitron',sans-serif;font-weight:700;text-shadow:0 0 16px rgba(0,255,200,0.55);line-height:1.3;">final_exam<br>_score</div>
          <div style="color:#3d4d72;font-size:11px;">Range: 0 – 100</div>
        </div>
      </div>
    </div>
  </div>

  <!-- METRICS -->
  <div class="section">
    <div class="section-label">Model Performance</div>
    <div class="metrics-grid">
      <div class="metric m1">
        <div class="metric-name">MAE</div>
        <div class="metric-val">4.12</div>
        <div class="metric-label">Mean Abs Error</div>
      </div>
      <div class="metric m2">
        <div class="metric-name">MSE</div>
        <div class="metric-val">27.85</div>
        <div class="metric-label">Mean Sq Error</div>
      </div>
      <div class="metric m3">
        <div class="metric-name">RMSE</div>
        <div class="metric-val">5.28</div>
        <div class="metric-label">Root MSE</div>
      </div>
      <div class="metric m4">
        <div class="metric-name">R²</div>
        <div class="metric-val">0.83</div>
        <div class="metric-label">R² Score</div>
      </div>
    </div>
  </div>

  <!-- HOW IT WORKS -->
  <div class="section">
    <div class="section-label">How It Works</div>
    <div class="steps">
      <div class="step"><div class="step-num">01</div><div class="step-text"><strong>Data Loading</strong> — reads CSV, separates features and target column</div></div>
      <div class="step"><div class="step-num">02</div><div class="step-text"><strong>Preprocessing</strong> — normalizes input features for stable convergence</div></div>
      <div class="step"><div class="step-num">03</div><div class="step-text"><strong>Gradient Descent</strong> — iteratively minimizes MSE loss over N epochs</div></div>
      <div class="step"><div class="step-num">04</div><div class="step-text"><strong>Prediction</strong> — outputs final exam score per student</div></div>
      <div class="step"><div class="step-num">05</div><div class="step-text"><strong>Evaluation</strong> — computes MAE, MSE, RMSE, and R² score</div></div>
    </div>
  </div>

  <!-- PROJECT STRUCTURE -->
  <div class="section">
    <div class="section-label">Project Structure</div>
    <div class="tree">
      <span class="t-dir">📁 project/</span><br>
      &nbsp;&nbsp;├── <span class="t-main">main.py</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#2e3d5c;"># Entry point</span><br>
      &nbsp;&nbsp;├── <span class="t-file">data_generator.py</span>&nbsp;&nbsp;&nbsp;<span style="color:#2e3d5c;"># Sample data generator</span><br>
      &nbsp;&nbsp;├── <span class="t-dir">📁 data/</span><br>
      &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── <span class="t-file">student_scores.csv</span><br>
      &nbsp;&nbsp;├── <span class="t-file">requirements.txt</span><br>
      &nbsp;&nbsp;└── <span class="t-file">README.html</span>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    Built with ❤️ &nbsp;·&nbsp; <span>Pure Python</span> &nbsp;·&nbsp; No ML Libraries &nbsp;·&nbsp; <span>Custom Gradient Descent</span>
  </div>

</div>

<script>
  // Generate floating particles
  const container = document.getElementById('particles');
  const colors = ['#00ffc8','#7b5fff','#ff4fd8','#ffd166'];
  for (let i = 0; i < 40; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    p.style.left = Math.random() * 100 + 'vw';
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    p.style.animationDuration = (8 + Math.random() * 14) + 's';
    p.style.animationDelay = (Math.random() * 12) + 's';
    p.style.width = p.style.height = (Math.random() > 0.5 ? '2px' : '3px');
    container.appendChild(p);
  }

  // Stagger section fade-ins
  document.querySelectorAll('.section').forEach((s, i) => {
    s.style.animationDelay = (i * 0.1) + 's';
  });
</script>
</body>
</html>
