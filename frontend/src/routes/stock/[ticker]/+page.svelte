<script>
  import { page } from "$app/stores";
  import { onDestroy } from "svelte";

  let ticker;
  let userData;

    // Subscribe to the route parameters
    const unsubscribe = page.subscribe(($page) => {
    ticker = $page.params.ticker;
    console.log(ticker)
});


</script>

<div class="bg-black min-h-screen text-white">
    <div class="py-5 px-25">
        <nav class="text-white shadow-md py-3">
            <div class="container mx-auto flex justify-between items-center px-6">
                
                <!-- Left Spacer (Keeps Centered Title in Place) -->
                <div class="w-1/3"></div>
    
                <!-- Website Name (Centered) -->
                <div class="w-1/3 text-center text-xl font-bold">
                    <a href="/" class="hover:text-blue-500 underline">Understocks</a>
                </div>
    
                <!-- Right Menu -->
                <div class="w-1/3 flex justify-end space-x-6 text-lg font-medium">
                    <a href="/" class="hover:text-blue-500">How it works</a>
                    <a href="/" class="hover:text-blue-500">Contact</a>
                </div>
    
            </div>
        </nav>
    </div>

</div>