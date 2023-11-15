window.onload = function () {
  console.log(
    "Hi! We're just here to force dark mode because we like it. We don't believe that there will be any accessibility issues with this, but if there are, please let us know by filing an Issue on GitHub or HuggingFace. https://github.com/jtpotato/firetrace/issues/new"
  );
  document.body.classList.add("dark");
  document.body.style.backgroundColor = "#0b0f19";

  let formData = new FormData();

  // get user agent
  let ua = navigator.userAgent.toLowerCase();
  // get time zone name (for geographic location reasons)
  let timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  let time = new Date().toUTCString();

  formData.append("entry.1589624473", "firetrace");
  formData.append("entry.1274276072", timezone);
  formData.append("entry.1686986475", time);
  formData.append("entry.1334016412", ua);

  fetch(
    "https://docs.google.com/forms/u/0/d/e/1FAIpQLScQqeT4NGpCGj5Uvjy5yLtptGuPUQFFuHSzVSZjySyGNyE8gw/formResponse",
    {
      method: "POST",
      mode: "no-cors",
      body: formData,
    }
  );
}
