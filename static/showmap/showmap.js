const mapContainer = document.getElementById("map"); // 지도를 표시할 div
const locbtn = document.getElementById("locbtn");
const locspan = document.getElementById("locspan");
const findbtn = document.getElementById("findbtn");
const anntable = document.getElementById("anntable");
const anndiv = document.getElementById("anndiv");

var x = 0;
var y = 0;
mapOption = {
  center: new kakao.maps.LatLng(36.321655, 127.378953), // 지도의 중심좌표
  level: 7, // 지도의 확대 레벨
};
// 지도를 생성합니다
const map = new kakao.maps.Map(mapContainer, mapOption);

findmyloc = () => {
  navigator.geolocation.getCurrentPosition(f);
};

function f(pos) {
  x = pos.coords.latitude;
  y = pos.coords.longitude;
  // console.log(x, y);
  locspan.innerText = `x:${x} y:${y}`;
  const moveloc = new kakao.maps.LatLng(x, y);
  map.setLevel(7);
  map.setCenter(moveloc);
  map.panTo(moveloc);
  var level = map.getLevel();
  const imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png";
  (imageSize = new kakao.maps.Size(64, 69)), (imageOption = { offset: new kakao.maps.Point(27, 69) });
  const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
  const markerpos = new kakao.maps.LatLng(x, y);
  const marker = new kakao.maps.Marker({
    position: markerpos,
    image: markerImage,
  });
  marker.setMap(map);
}

function ff() {
  n = document.getElementById("number").value;
  // anndiv.innerHTML = "";
  // loading_layer.style.display = "inline";
  if (1 === 0) {
    alert("위치를 모름");
    return;
  } else {
    fetch(`/showmapjson?&n=${n}&cx=${x}&cy=${y}`)
      .then((res) => res.json())
      .then((res) => {
        // console.log(data);
        ann_list = res["anns_list"];

        for (ann of ann_list) {
          try {
            const ann_dom = document.createElement("tr");
            const distance = ann.distance < 1000 ? ann.distance + "m" : (ann.distance / 1000).toFixed(2) + "km";
            const title = ann.title.length < 22 ? ann.title : ann.title.substr(0, 18) + "....";
            ann_dom.innerHTML = `<td>${distance}</td> <td>${title}</td>  <td><a href=/showdetail/${ann.ann_no}>바로가기</a></td>`;
            const obj = { content: `div${ann.title}</div>`, lating: new kakao.maps.LatLng(ann.y, ann.x) };
            const marker = new kakao.maps.Marker({ position: obj.lating });
            const infowindow = new kakao.maps.InfoWindow({
              content: obj.content,
            });
            kakao.maps.event.addListener(marker, "mouseover", makeOverListener(map, marker, infowindow));
            kakao.maps.event.addListener(marker, "mouseout", makeOutListener(infowindow));
            marker.setMap(map);
            anntable.appendChild(ann_dom);
          } catch (e) {
            continue;
          }
        }
      })
      .catch((e) => console.log(e))
      .finally(() => {
        // loading_layer.style.display = "none";
      });
  }
}

function makeOverListener(map, marker, infowindow) {
  return function () {
    infowindow.open(map, marker);
  };
}

function makeOutListener(infowindow) {
  return function () {
    infowindow.close();
  };
}

locbtn.addEventListener("click", findmyloc);
findbtn.addEventListener("click", ff);
console.clear();
