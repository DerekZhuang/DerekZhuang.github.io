// Figure viewer: click a figure to see it large. Without JavaScript the
// link simply opens the image file.
(function () {
  if (!window.HTMLDialogElement) return;
  var dlg = document.createElement("dialog");
  dlg.className = "lb";
  dlg.setAttribute("aria-label", "Figure, enlarged");
  dlg.innerHTML = '<div class="stage"><img alt=""><p></p></div><button type="button">Close</button>';
  document.body.appendChild(dlg);
  var img = dlg.querySelector("img");
  var cap = dlg.querySelector("p");

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a.zoom") : null;
    if (!a) return;
    e.preventDefault();
    var small = a.querySelector("img");
    var fig = a.closest("figure");
    var fc = fig ? fig.querySelector("figcaption") : null;
    img.src = a.getAttribute("href");
    img.alt = small ? small.alt : "";
    var num = fc ? fc.querySelector("b") : null;
    cap.textContent = fc ? (num ? num.textContent + ". " + fc.textContent.slice(num.textContent.length) : fc.textContent) : "";
    try { dlg.showModal(); } catch (err) { window.location.href = a.href; }
  });
  dlg.addEventListener("click", function () { dlg.close(); });
})();
