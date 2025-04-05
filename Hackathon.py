<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Learning Path Dashboard</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #f9f9f9;
      margin: 0;
      padding: 30px;
    }

    h1 {
      text-align: center;
      color: #2c3e50;
    }

    .container {
      max-width: 900px;
      margin: auto;
    }

    .card {
      background: #fff;
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }

    .card h2 {
      color: #2980b9;
    }

    .resource-list {
      list-style: none;
      padding: 0;
    }

    .resource-list li {
      padding: 8px 0;
    }

    .progress {
      color: green;
      font-weight: bold;
    }

    .form-group {
      margin: 15px 0;
    }

    input, select {
      padding: 8px;
      width: 100%;
      box-sizing: border-box;
      margin-top: 5px;
    }

    button {
      background: #3498db;
      color: white;
      padding: 10px 16px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      margin-top: 10px;
    }

    button:hover {
      background: #2980b9;
    }

    .form-section {
      margin-top: 40px;
    }

    label {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Learning Path Dashboard</h1>

  <div class="container" id="dashboard">
    <!-- Skills will load here -->
  </div>

  <div class="container form-section">
    <div class="card">
      <h2>Add New Skill & Resources</h2>
      <div class="form-group">
        <label>Skill Name</label>
        <input type="text" id="skillName">
      </div>

      <div class="form-group">
        <label>Resource Title</label>
        <input type="text" id="resourceTitle">
      </div>

      <div class="form-group">
        <label>Resource Type</label>
        <select id="resourceType">
          <option value="pdf">PDF</option>
          <option value="word">Word</option>
          <option value="video">Video</option>
          <option value="link">Hyperlink</option>
        </select>
      </div>

      <div class="form-group">
        <label>Estimated Reading Time (in minutes)</label>
        <input type="number" id="readingTime">
      </div>

      <button onclick="addSkill()">Add to Dashboard</button>
    </div>
  </div>

  <script>
    const skills = [];

    function renderDashboard() {
      const dashboard = document.getElementById("dashboard");
      dashboard.innerHTML = '';

      skills.forEach(skill => {
        let totalTime = 0;
        const card = document.createElement('div');
        card.className = 'card';

        let html = <h2>${skill.name}</h2><ul class="resource-list">;

        skill.resources.forEach(r => {
          html += <li>📄 ${r.title} (${r.type}) – ${r.time} min</li>;
          totalTime += r.time;
        });

        html += </ul><p class="progress">📊 Total Time: ${totalTime} minutes</p>;
        card.innerHTML = html;
        dashboard.appendChild(card);
      });
    }

    function addSkill() {
      const skillName = document.getElementById('skillName').value.trim();
      const resourceTitle = document.getElementById('resourceTitle').value.trim();
      const resourceType = document.getElementById('resourceType').value;
      const readingTime = parseInt(document.getElementById('readingTime').value);

      if (!skillName || !resourceTitle || isNaN(readingTime)) {
        alert("Please fill all fields properly.");
        return;
      }

      let skill = skills.find(s => s.name === skillName);

      if (!skill) {
        skill = { name: skillName, resources: [] };
        skills.push(skill);
      }

      skill.resources.push({
        title: resourceTitle,
        type: resourceType,
        time: readingTime
      });

      renderDashboard();

      // Clear form
      document.getElementById('skillName').value = '';
      document.getElementById('resourceTitle').value = '';
      document.getElementById('resourceType').value = 'pdf';
      document.getElementById('readingTime').value = '';
    }

    // Load empty dashboard on start
    renderDashboard();
  </script>
</body>
</html>