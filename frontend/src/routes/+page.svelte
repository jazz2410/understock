<script>
	import Footer from "$lib/Footer.svelte";
    import { goto } from '$app/navigation';
</script>
<section class=" flex flex-col lg:flex-row items-center justify-between px-6 py-16 max-w-2xl mx-auto">
    <!-- Left Side (Text) -->
    <div class="text-center lg:text-left max-w-lg">
      <h1 class="text-4xl font-bold text-white">Find undervalued stocks</h1>
      <p class="mt-4 text-lg text-gray-300">Find daily updated fair value based on discounted Cashflow
                                              analysis
                                              and Will Graham evaluation
      </p>
      <button on:click={() => goto('/stocks')} class="px-6 py-5 my-3 rounded-lg bg-orange-500 hover:bg-orange-600 text-black font-semibold shadow-md 
               transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 
               focus:ring-orange-400 dark:text-white cursor-pointer">
        See undervalued stocks
</button>

    </div>
  
    <!-- Right Side (Image) -->
    <div class="mt-8 lg:mt-0">
        <p>this is the right side</p>
        <a href="/stocks" class="hover:text-blue-500 ">Check undervalued stocks</a>
    </div>
  </section>
<div class="mt-50">
  <Footer></Footer>
</div>