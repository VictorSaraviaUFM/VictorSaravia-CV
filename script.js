(function () {
  var C = window.CONTENT, P = C.profile, $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); };
  var btn = function (href, label, cls, ext) { return '<a class="btn ' + (cls || "") + '" href="' + href + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + '>' + label + "</a>"; };

  // Hero
  $("h-eyebrow").textContent = "Universidad Francisco Marroquín · Guatemala";
  $("h-name").textContent = P.name; $("h-role").textContent = P.headline; $("h-lead").textContent = P.tagline;
  $("h-cta").innerHTML = btn("#projects", "View Projects", "primary") + btn(P.resume, "Download Resume", "", false).replace("<a ", "<a download ") +
    btn(P.github, "GitHub", "", true) + btn(P.linkedin, "LinkedIn", "", true) + btn("#contact", "Contact");
  var img = $("h-photo");
  img.onerror = function () { img.hidden = true; $("h-init").hidden = false; };  // initials stand-in until photo exists
  img.src = P.photo;

  // About
  $("about-text").innerHTML = C.about.map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("");
  $("traits").innerHTML = C.traits.map(function (t) { return "<li><strong>" + esc(t[0]) + "</strong><span>" + esc(t[1]) + "</span></li>"; }).join("");

  // Projects
  $("project-grid").innerHTML = C.projects.map(function (p) {
    var priv = p.status.indexOf("Private") === 0;
    var link = p.repo ? '<a class="btn small" href="' + p.repo + '" target="_blank" rel="noopener">View on GitHub →</a>'
                      : '<span class="note">' + esc(p.note || "Repository available upon request") + "</span>";
    return '<article class="card"><div class="flow" aria-label="Architecture overview">' + p.flow.map(function (f) { return "<span>" + esc(f) + "</span>"; }).join('<i aria-hidden="true">→</i>') + "</div>" +
      '<div class="meta"><span class="pill area">' + esc(p.area) + '</span><span class="pill' + (priv ? " priv" : "") + '">' + esc(p.status) + '</span><span class="pill">' + esc(p.team) + "</span></div>" +
      "<h3>" + esc(p.name) + '</h3><p class="type">' + esc(p.type) + "</p><p>" + esc(p.summary) + "</p>" +
      "<ul>" + p.highlights.map(function (h) { return "<li>" + esc(h) + "</li>"; }).join("") + "</ul>" +
      '<div class="tags">' + p.tags.map(function (t) { return "<span>" + esc(t) + "</span>"; }).join("") + "</div>" + '<div class="card-foot">' + link + "</div></article>";
  }).join("");

  // Skills
  $("skills-grid").innerHTML = C.skills.map(function (g) {
    return '<div class="skill"><h3>' + esc(g.group) + "</h3>" + g.items.map(function (i) { return '<p><span class="lbl">' + esc(i[0]) + "</span>" + esc(i[1]) + "</p>"; }).join("") + "</div>";
  }).join("");

  // Education, languages, certs, interests
  $("edu").innerHTML = C.education.map(function (e) {
    return '<div class="row"><div><h3>' + esc(e.school) + "</h3><p>" + esc(e.detail) + "</p>" + (e.extra ? '<p class="muted">' + esc(e.extra) + "</p>" : "") + '</div><span class="date">' + esc(e.dates) + "</span></div>";
  }).join("");
  $("langs").textContent = "Languages: " + C.languages;
  $("certs").innerHTML = C.certifications.map(function (c) {
    return "<li><div><h3>" + esc(c.name) + '</h3><p class="muted">' + esc(c.issuer) + " · " + esc(c.date) + "</p></div>" +
      (c.link ? '<a href="' + c.link + '" target="_blank" rel="noopener">View credential →</a>' : '<span class="muted">[CREDENTIAL LINK]</span>') + "</li>";
  }).join("");
  $("interests-grid").innerHTML = C.interests.map(function (i) { return '<div class="tile"><h3>' + esc(i[0]) + "</h3><p>" + esc(i[1]) + "</p></div>"; }).join("");

  // Contact
  $("c-cta").innerHTML = btn("mailto:" + P.email, esc(P.email), "primary") + btn("tel:" + P.phoneHref, esc(P.phone)) + btn(P.linkedin, "LinkedIn", "", true) + btn(P.github, "GitHub", "", true);
  $("year").textContent = new Date().getFullYear();

  // Theme toggle
  var root = document.documentElement, tb = $("theme"), tl = $("theme-label");
  function sync() { var d = root.getAttribute("data-theme") === "dark"; tl.textContent = d ? "Light mode" : "Dark mode"; tb.setAttribute("aria-pressed", String(d)); tb.setAttribute("aria-label", "Switch to " + (d ? "light" : "dark") + " mode"); }
  tb.addEventListener("click", function () {
    var n = root.getAttribute("data-theme") === "dark" ? "light" : "dark"; root.setAttribute("data-theme", n);
    try { localStorage.setItem("theme", n); } catch (e) {} sync();
  });
  sync();
})();
