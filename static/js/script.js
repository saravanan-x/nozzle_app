
const tabs = document.querySelectorAll('.tab');
const panels = document.querySelectorAll('.tab-panel');
const sideItems = document.querySelectorAll('.sidebar-item');

function setTab(i) {
  tabs.forEach((t, idx) => t.classList.toggle('active', idx === i));
  panels.forEach((p, idx) => p.classList.toggle('active', idx === i));
  sessionStorage.setItem('nozzle_tab', i);
}

function activeSidebar(el, tabIndex) {
  sideItems.forEach(s => s.classList.remove('active'));
  el.classList.add('active');
  setTab(tabIndex);
}

// Restore tab on reload
window.addEventListener('load', () => {
  const saved = sessionStorage.getItem('nozzle_tab');
  if (saved !== null) setTab(parseInt(saved));
});

// Save active tab before submit
document.getElementById('mainForm').addEventListener('submit', () => {
  const active = [...tabs].findIndex(t => t.classList.contains('active'));
  sessionStorage.setItem('nozzle_tab', active);
});

//img viewer
let scale = 1;
let startX = 0, startY = 0;
let translateX = 0, translateY = 0;
let isDragging = false;

const viewer = document.getElementById("imgViewer");
const img = document.getElementById("viewerImg");

// OPEN VIEWER
document.querySelectorAll(".clickable-img").forEach(el => {
  el.addEventListener("click", () => {
    viewer.style.display = "block";
    img.src = el.src;

    // reset state
    scale = 1;
    translateX = 0;
    translateY = 0;
    updateTransform();
  });
});

// APPLY TRANSFORM
function updateTransform() {
  img.style.transform =
    `translate(${translateX}px, ${translateY}px) scale(${scale})`;
}

// ZOOM FUNCTIONS
function zoomIn() {
  scale *= 1.2;
  updateTransform();
}

function zoomOut() {
  scale /= 1.2;
  updateTransform();
}

function resetZoom() {
  scale = 1;
  translateX = 0;
  translateY = 0;
  updateTransform();
}

// MOUSE WHEEL ZOOM (ZOOM AT CURSOR)
img.addEventListener("wheel", (e) => {
  e.preventDefault();

  const rect = img.getBoundingClientRect();
  const offsetX = e.clientX - rect.left;
  const offsetY = e.clientY - rect.top;

  const zoom = e.deltaY < 0 ? 1.1 : 0.9;

  translateX -= offsetX * (zoom - 1);
  translateY -= offsetY * (zoom - 1);

  scale *= zoom;
  updateTransform();
});

// DRAG (PAN)
img.addEventListener("mousedown", (e) => {
  isDragging = true;
  startX = e.clientX - translateX;
  startY = e.clientY - translateY;
  img.style.cursor = "grabbing";
});

window.addEventListener("mousemove", (e) => {
  if (!isDragging) return;

  translateX = e.clientX - startX;
  translateY = e.clientY - startY;
  updateTransform();
});

window.addEventListener("mouseup", () => {
  isDragging = false;
  img.style.cursor = "grab";
});

// CLOSE VIEWER
function closeViewer() {
  viewer.style.display = "none";
}

// DOUBLE CLICK RESET
img.addEventListener("dblclick", resetZoom);

// CLICK OUTSIDE CLOSE
viewer.addEventListener("click", (e) => {
  if (e.target === viewer) closeViewer();
});


    // Open Formulas Modal
    function openFormulasModal() {
        document.getElementById('formulasModal').style.display = 'block';
        // Re-render MathJax if you use it
        if (typeof MathJax !== 'undefined') {
            MathJax.typesetPromise();
        }
    }
    
    // Close Formulas Modal
    function closeFormulasModal() {
        document.getElementById('formulasModal').style.display = 'none';
    }
    
    // Close when clicking outside the modal
    window.onclick = function(event) {
        const modal = document.getElementById('formulasModal');
        if (event.target === modal) {
            closeFormulasModal();
        }
    }
