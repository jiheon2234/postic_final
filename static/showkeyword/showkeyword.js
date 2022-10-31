const sido_input = document.getElementById("sido_input");
const sido_btn = document.getElementById("sido_btn");
const occ_input = document.getElementById("occ_input");
const occ_btn = document.getElementById("occ_btn");
const container = document.getElementById("container");
const ranking = document.getElementById("ranking");

sido_btn.addEventListener("click", f);
occ_btn.addEventListener("click", f);
// no async
function f(event) {
  container.innerHTML = "";
  ranking.innerHTML = "";
  if (event.target.id == "sido_btn") {
    const sido = sido_input.value.trim();
    const sido_num = sido_dict[sido];
    if (sido_num === undefined) {
      alert("목록에 없음");
      return;
    }
    url = `showkeywordjson?&kind=sido&momid=${sido_num}`;
  } else {
    const occ_num = occ_input.value;
    if (0 < occ_input < 14) {
      url = `showkeywordjson?&kind=occ&occ_num=${occ_num}`;
    } else {
      alert("something wrong ");
      return;
    }
  }

  loading_layer.style.display = "block";

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      const words = data.data;
      const chart = anychart.tagCloud(words);
      chart.container("container");
      chart.draw();
      for (let i = 0; i < 20; i++) {
        const div = make_div(i, words[i].x, words[i].value);
        ranking.appendChild(div);
      }
    })
    .catch(console.log)
    .finally(() => (loading_layer.style.display = "None"));
}

const sido_dict = {
  서울특별시: 11,
  부산광역시: 21,
  대구광역시: 22,
  인천광역시: 23,
  광주광역시: 24,
  대전광역시: 25,
  울산광역시: 26,
  세종특별자치시: 29,
  경기도: 31,
  강원도: 32,
  충청북도: 33,
  충청남도: 44,
  전라북도: 35,
  전라남도: 36,
  경상북도: 37,
  경상남도: 38,
  제주특별자치도: 39,
};

occ_obj = {
  "01": "경영·사무·금융·보험",
  "02": "연구 및 공학기술",
  "03": "교육·법률·사회복지·경찰·소방 및 군인",
  "04": "보건·의료",
  "05": "예술·디자인·방송·스포츠",
  "06": "미용·여행·숙박·음식·경비·돌봄·청소",
  "07": "영업·판매·운전·운송",
  "08": "건설·채굴",
  "09": "설치·정비·생산-기계·금속·재료",
  10: "설치·정비·생산-전기·전자·정보통신",
  11: "설치·정비·생산-화학·환경·섬유·의복·식품가공",
  12: "설치·정비·생산-인쇄·목재·공예 및 제조 단순",
  13: "농림어업직",
};

function make_div(rank, text, value) {
  const div = document.createElement("div");
  div.innerHTML = `<span style="color:red; font-size:1.5em">${rank}</span>${text} :${value} `;
  if (rank < 10) {
    div.style.backgroundColor = "black";
    div.style.color = "white";
  }
  return div;
}
