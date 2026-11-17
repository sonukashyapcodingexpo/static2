(function () {
  var burger = document.querySelector(".burger");
  var nav = document.querySelector(".nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("nav-open", open);
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-open");
      });
    });
  }

  function fitDrop(drop) {
    var panel = drop.querySelector(".drop-panel");
    if (!panel) return;
    if (!window.matchMedia("(min-width: 1040px)").matches) {
      panel.style.left = "";
      panel.style.right = "";
      return;
    }
    panel.style.left = "0px";
    panel.style.right = "auto";
    var rect = panel.getBoundingClientRect();
    if (rect.width < 40) return;
    var limit = window.innerWidth - 16;
    if (rect.right > limit) {
      var next = rect.left - (rect.right - limit);
      if (next < 16) next = 16;
      panel.style.left = (next - rect.left) + "px";
    }
  }

  document.querySelectorAll(".drop > button").forEach(function (button) {
    button.addEventListener("click", function (event) {
      if (window.matchMedia("(min-width: 1040px)").matches) return;
      event.preventDefault();
      var drop = button.parentElement;
      var open = drop.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  document.querySelectorAll(".drop").forEach(function (drop) {
    drop.addEventListener("mouseenter", function () { fitDrop(drop); });
    drop.addEventListener("focusin", function () { fitDrop(drop); });
  });

  document.querySelectorAll("[data-form]").forEach(function (form) {
    var file = form.querySelector('input[type="file"]');
    var nameEl = form.querySelector("[data-file-name]");
    var emptyLabel = nameEl ? nameEl.textContent : "";
    function checkFile() {
      if (!file) return;
      var picked = file.files && file.files[0];
      if (!picked) {
        file.setCustomValidity(file.required ? "Upload a PDF, DOC, or DOCX under 5 MB." : "");
        if (nameEl) nameEl.textContent = emptyLabel;
        return;
      }
      var okType = /\.(pdf|doc|docx)$/i.test(picked.name);
      var okSize = picked.size <= 5 * 1024 * 1024;
      if (!okType) file.setCustomValidity("Upload a PDF, DOC, or DOCX.");
      else if (!okSize) file.setCustomValidity("CV must be 5 MB or smaller.");
      else file.setCustomValidity("");
      if (nameEl) nameEl.textContent = picked.name;
    }
    if (file) file.addEventListener("change", checkFile);
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      checkFile();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      form.classList.add("is-sent");
    });
  });

  var onScroll = function () {
    document.body.classList.toggle("is-scrolled", window.scrollY > 24);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduce && "IntersectionObserver" in window) {
    document.documentElement.classList.add("js");
    var nodes = document.querySelectorAll(".section, .stat-strip, .cta, .quote, .reason");
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        seen.unobserve(entry.target);
      });
    }, { threshold: 0.16 });
    nodes.forEach(function (el) {
      el.classList.add("await");
      var rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.92 && rect.bottom > 0) el.classList.add("is-in");
      else seen.observe(el);
    });
  }

  function paintCount(el, value) {
    var pad = parseInt(el.getAttribute("data-pad") || "0", 10);
    var text = String(Math.max(0, Math.round(value)));
    while (pad > text.length) text = "0" + text;
    el.textContent = text;
  }

  document.querySelectorAll("[data-count]").forEach(function (el) {
    var target = parseFloat(el.getAttribute("data-count"));
    if (!isFinite(target)) return;
    if (reduce) {
      paintCount(el, target);
      return;
    }
    var played = false;
    var play = function () {
      if (played) return;
      played = true;
      var start = performance.now();
      var duration = Math.min(1600, 900 + target * 6);
      var tick = function () {
        var t = Math.min(1, (performance.now() - start) / duration);
        var eased = 1 - Math.pow(1 - t, 3);
        paintCount(el, t < 1 ? target * eased : target);
        if (t < 1) setTimeout(tick, 16);
      };
      paintCount(el, 0);
      setTimeout(tick, 16);
    };
    if (!("IntersectionObserver" in window)) {
      play();
      return;
    }
    var watch = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        play();
        watch.unobserve(el);
      });
    }, { threshold: 0.5 });
    var rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.92 && rect.bottom > 0) play();
    else watch.observe(el);
  });

  document.querySelectorAll(".faq-item button").forEach(function (button) {
    button.addEventListener("click", function () {
      var item = button.parentElement;
      var open = item.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
})();
