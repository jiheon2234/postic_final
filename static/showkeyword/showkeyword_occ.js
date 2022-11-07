const current_region = document.getElementById("current_region");
const sub_btn = document.getElementById("sub_btn");
const loading_layer = document.getElementById("loading_layer");
const container = document.getElementById("container");

region = 0;
occ = 0;
function f(event) {
  region = event.target.value;
}

function find_occ() {
  const occ_list = document.getElementsByName("occ");
  occ = 0;
  occ_list.forEach((n) => {
    if (n.checked) {
      occ |= 1 << (n.value - 1);
      return 1;
      // break
    }
    return 0;
  });
}

function draw_cloud() {
  find_occ();

  if (region == 0 || occ == 0) {
    alert("선택되지 않음");
    return;
  }
  container.innerHTML = "";
  url = `showkeywordjson?&kind=both&occ_num=${occ}&momid=${region}`;
  loading_layer.style.display = "block";
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      const words = data.data;
      // console.log(words);
      const chart = anychart.tagCloud(words);
      chart.container("container");
      chart.draw();
    })
    .catch(console.log)
    .finally(() => (loading_layer.style.display = "None"));
}

sub_btn.addEventListener("click", draw_cloud);
