<?php


require "vendor/autoload.php";

use Elasticsearch\ClientBuilder;

$client = ClientBuilder::create()
    ->setHosts(['localhost:9200'])
    ->build();

echo "<pre>";

/*
 * gelen postu eklemek
 */

$name = $_POST['name'];
$surname = $_POST['surname'];


$reuslt = $client->index([
   'index' => 'ders',
   'type' => 'elastic',
    'body' => $_POST
]);


print_r($reuslt);










//$response = $client->info();
//
//echo $response['version']['number']; // 8.0.0


/*
 * tekil indexleme
 */

//
//$params = [
//    'index' => 'my_index',
//    'id' => 'my_id',
//    'body' => ['test' => 'abc']
//];
//
//$result = $client->index($params);


/*
 *  toplu indexleme
 */
//for ($i = 0; $i < 100; $i++)
//{
//    $params['body'][] = [
//      'index' => [
//          '_index' => 'my_index'
//      ]
//    ];
//
//    $params['body'][] = [
//      'my_field' => 'my_value',
//      'second_field' => 'some more values'
//    ];
//}
//
//$result = $client->bulk($params);



/*
 * tekli getirme
 */

//$params = [
//    'index' => 'my_index',
//    'id' => 'my_id'
//    ];
//
//$result = $client->get($params);


/*
 * tekli getirme veya arama sonucu yoksa hata mesajı verdirme
 */
//
//$params = [
//    'index' => 'my_index',
//    'id' => 'my_id'
//];
//try {
//
//    $result = $client->get($params);
//    print_r($result);
//}catch( \Elasticsearch\Common\Exceptions\Missing404Exception $e)
//{
//    printf('Document not found', $e->getMessage());
//}


/*
 *  güncelleme veya yeni field ekleme ve görüntüleme
 */
//
//$params = [
//  'index' => 'my_index',
//  'id' => 'my_id',
//  'body' => [
//     'doc' => [
//         'new_field' =>  'abc'
//     ]
//  ]
//];
//
//$result = $client->update($params);
//print_r($result);
//
//
//$params = [
//    'index' => 'my_index',
//    'id' => 'my_id'
//    ];
//
//$result1 = $client->get($params);
//print_r($result1);


/*
 *  item silmek ve var mı yok mu kontrol etmek - deleted
 */
////$params = [
////  'index' => 'my_index',
////  'id' => 'my_id'
////];
////
////$result = $client->delete($params);
////print_r($result);
//
//$params1 = [
//    'index' => 'my_index',
//    'id' => 'my_id'
//    ];
//
//
//try {
//
//    $result1 = $client->get($params1);
//    print_r($result1);
//}catch( \Elasticsearch\Common\Exceptions\Missing404Exception $e)
//{
//    printf('Document not found', $e->getMessage());
//}


/*
 *  search - arama
 */

//$params = [
//    'index' => 'my_index',
//    'id' => 'my_id',
//    'body' => ['test' => 'abc111']
//];
//
//$client->index($params);
//
//$params = [
//  'index' => 'my_index',
//  'body' => [
//   'query' => [
//       'match' => [
//           'test' => 'abc111'
//       ]
//     ]
//  ]
//];
//
//$result = $client->search($params);
//print_r($result);


/*
 *  fuzzy arama google arama mantığı gibi tek tuşla aramaya başlaıyor
 */


//$params = [
//    'index' => 'my_index',
//    'id' => 'my_id',
//    'body' => ['test' => 'abc111']
//];
//
//$client->index($params);
//
//$params = [
//   'index' => 'my_index',
//   'body' => [
//       'query' => [
//           'fuzzy' => [
//               'name' => [
//                   'value' => 'abc111'
//               ]
//           ]
//       ]
//   ]
//];
//
//$result = $client->search($params);
//print_r($result);