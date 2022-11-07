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
      all_cnt.innerHTML = `
      <style>
        .cnt-icon {
          font-size:1.2em;
          font-weight:bold;
          text-align: center;
          margin-top:30%;
        }
        .cnt-job {
          font-size:2.5em;
          font-weight:bold;
          text-align: center;
        }
        .cnt-circle {
          width: 350px;
          height: 350px;
          border: 30px solid transparent;
          border-radius: 50%;
          background-image: linear-gradient(#ffffff, #ffffff), linear-gradient(to top, #6a6aff, #8CBDED, #B4B4FF);
          background-origin: border-box;
          background-clip: content-box, border-box;
          margin:auto;
        }
      </style>
      <!--
      <div class="wrapper">
        <div class="circle"></div>
      </div>-->
      
      <div class = "cnt-circle">
        <p class = "cnt-icon">⚝ TOTAL ⚝</p>
        <p class = "cnt-job"> ${cnt} 건 </p>
      </div>
      `;
      if (child_sido) {
        detail_sido.replaceChildren();
        for (obj of child_sido) {
          let btn = createbtn(obj);
          // console.log(btn); <p class = "cnt-job">⚝ TOTAL ⚝ <br> ${cnt} 건</p>

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

  btn.style = `
  display: inline-block;
  padding: 8px 15px;
  font-size: 14px;
  cursor: pointer;
  text-align: center;	
  text-decoration: none;
  outline: none;
  color: rgb(28, 25, 31);
  background-color: #d3d3fe;
  border: none;
  border-radius: 8px;
  box-shadow: 0 5px #999;
  margin : 10px 5px 10px 5px;
  `;
  return btn;
}
