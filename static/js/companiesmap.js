ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map('map', {
        center: [59.87723890752992, 30.442120511878755],
        zoom: 12
    }, {
        searchControlProvider: 'yandex#search'
    })

    BX24.callMethod('crm.company.list', {select: ['TITLE', 'ID']}, function (res) {
        let Companies = res.answer.result
        BX24.callMethod('crm.address.list', {select: ['ADDRESS_1', 'ANCHOR_ID', 'CITY']}, function (res) {
            let Addresses = res.answer.result

            Companies.forEach(comp => {
                Addresses.forEach(address => {
                        if (comp['ID'] === address['ANCHOR_ID']) {
                            let obj_to_geocode = ymaps.geocode(`${address['CITY']}, ${address['ADDRESS_1']}`)
                            obj_to_geocode.then(function (res) {
                                let geocoded_obj = res.geoObjects.properties._data.metaDataProperty.GeocoderResponseMetaData.Point.coordinates
                                // Making balloon obj on map
                                myMap.geoObjects.add(new ymaps.Placemark([geocoded_obj[1], geocoded_obj[0]], {
                                    balloonContent: `<strong>${comp['TITLE']}</strong>` + `<br>` + `${address['CITY']}, ${address['ADDRESS_1']}`
                                }, {
                                    preset: 'islands#icon',
                                    iconColor: 'red'
                                }))
                            })
                        }
                    }
                )
            })
        })
    })
}

