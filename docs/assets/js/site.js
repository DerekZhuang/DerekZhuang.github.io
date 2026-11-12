// Figure viewer: click a figure to see it large. Without JavaScript the
// link simply opens the image file.
(function () {
  if (!window.HTMLDialogElement) return;
  // On a phone the viewer cannot show a figure any larger than the page
  // already does, so there the link opens the full-size image instead,
  // where it can be pinched and panned. Back returns to the page.
  var phone = window.matchMedia("(max-width: 600px)");
  var dlg = document.createElement("dialog");
  dlg.className = "lb";
  dlg.setAttribute("aria-label", "Figure, enlarged");
  dlg.innerHTML = '<div class="stage"><img alt=""><p></p></div><button type="button">Close</button>';
  document.body.appendChild(dlg);
  var img = dlg.querySelector("img");
  var cap = dlg.querySelector("p");

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a.zoom") : null;
    if (!a || phone.matches) return;
    e.preventDefault();
    var small = a.querySelector("img");
    var fig = a.closest("figure");
    var fc = fig ? fig.querySelector("figcaption") : null;
    img.src = a.getAttribute("href");
    img.alt = small ? small.alt : "";
    var num = fc ? fc.querySelector("b") : null;
    cap.textContent = fc ? (num ? num.textContent + ". " + fc.textContent.slice(num.textContent.length) : fc.textContent) : "";
    try {
      dlg.showModal();
      // keep the page behind the viewer from scrolling
      document.documentElement.classList.add("viewing");
    } catch (err) { window.location.href = a.href; }
  });
  dlg.addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("close", function () { document.documentElement.classList.remove("viewing"); });
})();
