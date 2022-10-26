const region_div = document.getElementById("region");
for (ch of region_div.children) {
  ch.addEventListener("click", f);
}

function f(event) {
  const region = event.target.value;
  fetch(`/regionjson?&region=${region}`)
    .then((res) => res.json())
    .then((data) => {
      // console.log(data);
      let { worktype_list, paytype_list, pay_avg_list } = data;
      chart1.updateSeries([
        {
          name: "test",
          data: pay_avg_list,
        },
      ]);
      chart2.updateSeries(paytype_list);
      chart3.updateSeries(worktype_list);
    });
}
