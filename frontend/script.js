// frontend/script.js
const API_BASE = "http://localhost:8000";

async function searchMovie() {
  const query = document.getElementById("searchInput").value;
  const res = await fetch(`${API_BASE}/search?query=${encodeURIComponent(query)}`);
  const data = await res.json();

  const container = document.getElementById("results");
  container.innerHTML = "";

  if (data.length === 0) {
    container.innerHTML = "<p>No results found.</p>";
    return;
  }

  data.forEach(movie => {
    const div = document.createElement("div");
    div.className = "movie-result";
    div.innerHTML = `
      <strong>${movie.title} (${movie.year})</strong>
      <button onclick="getRecommendations('${movie.slug}')">🎥 Recommend</button>
    `;
    container.appendChild(div);
  });
}

async function getRecommendations(slug) {
  const res = await fetch(`${API_BASE}/recommendations/${slug}`);
  const recs = await res.json();

  const container = document.getElementById("results");
  container.innerHTML = "<h3>🎯 Recommendations</h3>";

  recs.forEach(rec => {
    const div = document.createElement("div");
    div.className = "movie-recommendation";
    div.innerHTML = `
      <strong>${rec.title} (${rec.year})</strong>
      <button onclick="viewMovie('${rec.slug}')">💬 View Reviews</button>
    `;
    container.appendChild(div);
  });
}

async function getRoulette() {
  const res = await fetch(`${API_BASE}/roulette`);
  const movie = await res.json();
  viewMovie(movie.slug);
}

function viewMovie(slug) {
  window.location.href = `movie.html?slug=${slug}`;
}
