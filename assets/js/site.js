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

  document.querySelectorAll(".drop > button").forEach(function (button) {
    button.addEventListener("click", function (event) {
      if (window.matchMedia("(min-width: 1040px)").matches) return;
      event.preventDefault();
      var drop = button.parentElement;
      var open = drop.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  document.querySelectorAll("[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
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

  document.querySelectorAll(".faq-item button").forEach(function (button) {
    button.addEventListener("click", function () {
      var item = button.parentElement;
      var open = item.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
})();
