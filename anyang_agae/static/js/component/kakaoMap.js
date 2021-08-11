var mapContainer = document.getElementById('map') // 지도를 표시할 div
mapOption = {
  center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
  level: 3, // 지도의 확대 레벨
}

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption)

let markerList = []

let ps = new kakao.maps.services.Places()
function searchPlaces() {
  let keyword = $('#search_hospital').val()
  ps.keywordSearch(keyword, placesSearchCB)
}

function placesSearchCB(data, status) {
  if (status === kakao.maps.services.Status.OK) {
    console.log(data)
    displayPlaces(data)
  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    alert('검색 결과가 존재하지 않습니다.')
  } else if (status === kakao.maps.services.Status.ERROR) {
    alert('검색 결과 중 오류가 발생했습니다.')
    return
  }
}

function displayPlaces(data) {
  var hospitalList = document.querySelector('#hospitalList')
  var bounds = new kakao.maps.LatLngBounds() // 마커할 때 사용하는 함수
  for (let i = 0; i < data.length; i++) {
    let lat = data[i].y //위도
    let lng = data[i].x //경도
    let address_name = data[i]['address_name']
    let place_name = data[i]['place_name']

    const placePosition = new kakao.maps.LatLng(lat, lng)
    bounds.extend(placePosition) // bounds에 추가
    let marker = new kakao.maps.Marker({
      position: placePosition,
    }) // 마커에 추가

    marker.setMap(map)
    markerList.push(marker)

    const el = document.createElement('div')
    const itemStr = `
        <p class="placename">병원명 : ${place_name}</p>
        <p class="addressname">주소 : ${address_name}</p>
        <hr/>
      `
    el.innerHTML = itemStr

    let infowindow = new kakao.maps.InfoWindow({
      zIndex: 1,
    })

    //  인포 윈도우 클릭 이벤트 //
    kakao.maps.event.addListener(marker, 'click', function () {
      displayInfoWindows(marker, place_name, address_name, lat, lng)
    })
    kakao.maps.event.addListener(marker, 'click', function () {
      infowindow.close()
    })
    el.onclick = function () {
      displayInfoWindows(marker, place_name, address_name, lat, lng)
    }

    hospitalList.appendChild(el)
  }
  map.setBounds(bounds)
}

function displayInfoWindows(marker, place_name, address_name, lat, lng) {
  const placePosition = new kakao.maps.LatLng(lat, lng)
  var content = `
      <div style="padding: 30px;">
        병원명 : ${place_name} <br/>
        주소 : ${address_name} <br/>
        <a href="javascript:void(0);"
          id="submit_hospital"
          onClick="onClickValue('${place_name}');">등록</a>
      </div>
    `
  var infowindow = new kakao.maps.InfoWindow({
    position: placePosition,
    content: content,
    removable: true,
  })
  map.panTo(marker.getPosition()) // 해당 위치 불러옴
  // infowindow.setContent(content);
  infowindow.open(map, marker)
}

function onClickValue(place_name) {
  document.querySelector('#hospital').value = place_name
}
