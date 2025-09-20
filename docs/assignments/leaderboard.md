# Leaderboard

<div id="leaderboard-container">
  <div class="leaderboard-header">
    <h2>Top Performers</h2>
    <p>Automaatselt uueneb iga 5 minuti tagant</p>
  </div>
  
  <div id="loading">Laadin andmeid...</div>
  
  <table id="leaderboard-table" style="display: none;">
    <thead>
      <tr>
        <th>Koht</th>
        <th>Nimi</th>
        <th>Punkte</th>
        <th>Ülesandeid</th>
        <th>Badges</th>
      </tr>
    </thead>
    <tbody id="leaderboard-body">
    </tbody>
  </table>
</div>

<style>
.leaderboard-header {
  text-align: center;
  margin-bottom: 20px;
}

#leaderboard-table {
  width: 100%;
  border-collapse: collapse;
}

#leaderboard-table th {
  background-color: var(--md-primary-fg-color);
  color: white;
  padding: 10px;
  text-align: left;
}

#leaderboard-table td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

#leaderboard-table tr:hover {
  background-color: var(--md-accent-fg-color--transparent);
}

.badge {
  display: inline-block;
  padding: 2px 8px;
  margin: 2px;
  border-radius: 12px;
  font-size: 12px;
  background-color: var(--md-primary-fg-color);
  color: white;
}

.rank-1 { font-size: 1.5em; }
.rank-2 { font-size: 1.3em; }
.rank-3 { font-size: 1.1em; }
</style>

<script>
// Fetch leaderboard data from GitHub
async function loadLeaderboard() {
  try {
    // GitHub API endpoint for classroom data
    const response = await fetch('https://api.github.com/repos/mtalvik/automation/contents/leaderboard.json');
    const data = await response.json();
    const leaderboardData = JSON.parse(atob(data.content));
    
    displayLeaderboard(leaderboardData);
  } catch (error) {
    // Fallback to demo data
    displayLeaderboard(getDemoData());
  }
}

function getDemoData() {
  return [
    { name: "Alice", points: 980, completed: 12, badges: ["🚀 Speed Demon", "✨ Perfect Score", "🔥 Streak"] },
    { name: "Bob", points: 875, completed: 11, badges: ["✨ Perfect Score", "📚 Documenter"] },
    { name: "Charlie", points: 820, completed: 10, badges: ["🔥 Streak", "🎯 First Try"] },
    { name: "Diana", points: 750, completed: 9, badges: ["📚 Documenter"] },
    { name: "Eve", points: 720, completed: 8, badges: ["🎯 First Try"] }
  ];
}

function displayLeaderboard(data) {
  const tbody = document.getElementById('leaderboard-body');
  tbody.innerHTML = '';
  
  data.forEach((student, index) => {
    const row = document.createElement('tr');
    const rank = index + 1;
    row.className = rank <= 3 ? `rank-${rank}` : '';
    
    const medal = rank === 1 ? '🥇' : rank === 2 ? '🥈' : rank === 3 ? '🥉' : `${rank}.`;
    
    row.innerHTML = `
      <td>${medal}</td>
      <td>${student.name}</td>
      <td>${student.points}</td>
      <td>${student.completed}/15</td>
      <td>${student.badges.map(b => `<span class="badge">${b}</span>`).join('')}</td>
    `;
    
    tbody.appendChild(row);
  });
  
  document.getElementById('loading').style.display = 'none';
  document.getElementById('leaderboard-table').style.display = 'table';
}

// Load on page load
loadLeaderboard();

// Refresh every 5 minutes
setInterval(loadLeaderboard, 300000);
</script>

## Kuidas punkte teenida?

| Tegevus | Punkte |
|---------|--------|
| Ülesande lahendamine | 50-100 |
| Kõik testid rohelised | +20 |
| Esimene lahendus klassis | +30 |
| Koodi kvaliteet (linting) | +10 |
| Dokumentatsioon | +10 |
| Peer review | +5 |

## Badges

- **🚀 Speed Demon** - Lahendas ülesande < 1 tunni jooksul
- **✨ Perfect Score** - 100% testid läbitud esimesel katsel
- **🔥 Streak** - 5 ülesannet järjest õigel ajal
- **📚 Documenter** - Suurepärane dokumentatsioon
- **🎯 First Try** - Kõik testid läbitud esimesel pushil
- **💡 Helper** - Aitas teisi Discussions'is
- **🐛 Bug Hunter** - Leidis vea ülesandes

## Statistika

<div id="stats-container">
  <!-- Stats will be loaded here -->
</div>
