<?php


require "vendor/autoload.php";

use Elasticsearch\ClientBuilder;

$client = ClientBuilder::create()
    ->setHosts(['localhost:9200'])
    ->build();

//echo "<pre>";

/*
$iller = array('','Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale',
'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir',
'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir', 
'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 
'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya',
'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak',
'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak',
'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce');


for ($i = 0; $i < 81; $i++)
{
    $params['body'][] = [
      'index' => [
          '_index' => 'my_index'
      ]
    ];

    $params['body'][] = [
      'test' => $iller[$i]
    ];
}

$result = $client->bulk($params);
*/

$value = $_POST['value'];


/*
$params = [
    'index' => 'my_index',
    'id' => 'my_id',
    'body' => ['test' => 'abc111']
];

$client->index($params);
*/

/*
$params = [
  'index' => 'my_index',
  'body' => [
   'query' => [
       'match' => [
           'test' => $value
       ]
     ]
  ]
];


$result = $client->search($params);
*/



$result = $client->search([
    'index' => 'my_index',
    'body' => [
        'query' => [
            'fuzzy' =>[
                'test' => [
                    'value' => $value
                ]
            ]
        ]
    ]
]);



return json_encode($result["hits"]);




?>