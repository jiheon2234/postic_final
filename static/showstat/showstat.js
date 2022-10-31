const region_div = document.getElementById("region");
const detail_sido = document.getElementById("detail_sido");
const all_cnt = document.getElementById("all_cnt");
const loading_layer = document.getElementById("loading_layer");

// for (ch of region_div.children) {
//   ch.addEventListener("click", f);
// }

function f(event) {
  const region = event.target.value;
  loading_layer.style.display = "block";
  fetch(`/regionjson?&region=${region}`)
    .then((res) => res.json())
    .then((data) => {
      // console.log(data);
      let { worktype_list, paytype_list, pay_avg_list, child_sido } = data;
      let cnt = 0;
      for (let i = 0; i < worktype_list.length; i++) {
        cnt += worktype_list[i];
      }
      all_cnt.innerHTML = `<h1>${cnt}</h1>`;
      if (child_sido) {
        detail_sido.replaceChildren();
        for (obj of child_sido) {
          let btn = createbtn(obj);
          // console.log(btn);

          detail_sido.appendChild(btn);
        }
      } else {
        console.log(child_sido);
      }

      chart0.updateSeries([
        {
          name: "test0",
          data: worktype_list,
        },
      ]);
      chart1.updateSeries([
        {
          name: "test",
          data: pay_avg_list,
        },
      ]);
      chart2.updateSeries(paytype_list);
      chart3.updateSeries(worktype_list);
    })
    .finally(() => setTimeout(() => (loading_layer.style.display = "none"), 1000));
}

function createbtn(obj) {
  const btn = document.createElement("button");
  btn.innerText = obj.name;
  btn.value = obj.sido_no;
  btn.onclick = f;
  // btn.style='' 재언님이 만들어줄거임
  return btn;
}
