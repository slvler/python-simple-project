<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facedes\Response;




class BuildController extends Controller
{
    
    public function index(Request $request)
    {
      
        try{

            $req =  Http::withHeaders([
                'Authorization' => '563492ad6f917000010000014c2b39e50dad41ccb773546907e347b7',
            ])->get('https://api.pexels.com/v1/search?query=people', [
                'query' => $request->input('query'),
                'page' => $request->input('page'),
                'per_page' => $request->input('per_page'),
                'color' => $request->input('color')
            ]);

            
            if(!empty($req['photos']))
            {  
                return response( $req , 200 );

            }else {

                return response()->json(['error' => 'Photos Empty!'], 404);

            }

          
        } catch (\Exception $e) {

            return response()->json(['error' => $e->getMessage()], 500);
	        
        }
        

    }

    
    public function detail(Request $request)
    {

        try{

            $response = Http::withHeaders([
                'Authorization' => '563492ad6f917000010000014c2b39e50dad41ccb773546907e347b7',
            ])->get('https://api.pexels.com/videos/search?query=nature&per_page=1');
    

            
            if(!empty($response['videos']))
            {  
                return response( $response , 200 );

            }else {

                return response()->json(['error' => 'videos Empty!'], 404);

            }

          
        } catch (\Exception $e) {

            return response()->json(['error' => $e->getMessage()], 500);
	        
        }




    }


}
