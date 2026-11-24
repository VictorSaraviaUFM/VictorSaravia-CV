(function () {
  var root = document.documentElement;
  var btn = document.getElementById("theme-toggle");
  function apply(t) {
    root.setAttribute("data-theme", t);
    btn.setAttribute("aria-pressed", String(t === "dark"));
    btn.querySelector(".label").textContent = t === "dark" ? "Light mode" : "Dark mode";
  }
  apply(root.getAttribute("data-theme"));
  btn.addEventListener("click", function () {
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    try { localStorage.setItem("theme", next); } catch (e) {}
    apply(next);
  });

  // Photo fallback: if assets/profile.jpg is missing, show a placeholder.
  var img = document.getElementById("profile-img");
  function noPhoto() { document.getElementById("photo").classList.add("empty"); }
  img.addEventListener("error", noPhoto);
  if (img.complete && img.naturalWidth === 0) noPhoto();

  var d = window.SITE_DATA || {};
  var el = function (id) { return document.getElementById(id); };
  var tags = function (a, c) { return a.map(function (t) { return '<li class="' + c + '">' + t + "</li>"; }).join(""); };

  el("projects-list").innerHTML = (d.projects || []).map(function (p) {
    var priv = p.status !== "Public";
    var cta = p.repo
      ? '<a class="btn small" href="' + p.repo + '" target="_blank" rel="noopener">View on GitHub</a>'
      : '<span class="note">' + (p.repoNote || "") + "</span>";
    return '<article class="project"><div class="project-head"><h3>' + p.name + '</h3><span class="status ' + (priv ? "private" : "public") + '">' + p.status + "</span></div>" +
      '<p class="area">' + p.area + "</p><p>" + p.description + "</p>" +
      '<ul class="bullets">' + p.highlights.map(function (h) { return "<li>" + h + "</li>"; }).join("") + "</ul>" +
      '<ul class="tags" aria-label="Technologies">' + tags(p.tech, "tag") + "</ul>" + cta + "</article>";
  }).join("");

  el("skills-list").innerHTML = (d.skills || []).map(function (s) {
    return '<div class="skill"><h3>' + s.group + "</h3>" + (s.note ? '<p class="meta">' + s.note + "</p>" : "") +
      '<ul class="tags">' + tags(s.items, "tag") + "</ul>" + (s.detail ? '<p class="meta">' + s.detail + "</p>" : "") + "</div>";
  }).join("");

  el("education-list").innerHTML = (d.education || []).map(function (e) {
    return '<div class="edu"><h3>' + e.school + '</h3><p class="meta">' + e.period + "</p><p><strong>" + e.title + "</strong></p><p>" + e.detail + "</p></div>";
  }).join("");

  el("certs-list").innerHTML = (d.certifications || []).map(function (c) {
    var link = c.link ? '<a href="' + c.link + '" target="_blank" rel="noopener">Credential</a>' : '<span class="meta">[Add credential link]</span>';
    return '<li class="cert"><strong>' + c.name + '</strong><span class="meta">' + c.issuer + " · " + c.date + "</span>" + link + "</li>";
  }).join("");

  el("year").textContent = new Date().getFullYear();
})();
