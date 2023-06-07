<?php

require "vendor/autoload.php";

use Elasticsearch\ClientBuilder;

$client = ClientBuilder::create()
    ->setHosts(['localhost:9200'])
    ->build();

echo "<pre>";

//$result = $client->search([
//    'index' => 'ders',
//    'type' => 'elastic',
//    'body' => [
//        'query' => [
//            'multi_match' => [
//                "query" => $_POST["arama"],
//                "fields" => "name",
//                "fuzziness" => 2
//            ]
//        ]
//    ]
//]);

$result = $client->search([
    'index' => 'ders',
    'type' => 'elastic',
    'body' => [
        'query' => [
            'fuzzy' =>[
                'surname' => [
                    'value' => $_POST['arama']
                ]
            ]
        ]
    ]
]);


echo "<pre>";

print_r($result);