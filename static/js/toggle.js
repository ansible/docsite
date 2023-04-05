const currentPagePath = window.location.pathname;
const currentPageName = currentPagePath.substring(currentPagePath.lastIndexOf('/') + 1);

const pageToggle = document.getElementById('page-toggle');

if (pageToggle) {
  const redirectPageName = pageToggle.hasAttribute('data-target') ? pageToggle.getAttribute('data-target') : currentPageName;
  pageToggle.addEventListener('click', function() {
    window.location.href = './oldsite/' + redirectPageName;
  });
}
