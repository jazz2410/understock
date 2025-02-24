<script>
    let isOpen = false;
  </script>
  
  <nav class="text-white shadow-md py-3 bg-black sticky top-0 z-50">
      <div class="container mx-auto flex justify-between items-center px-6">
          
          <!-- Mobile Menu Button -->
          <button class="lg:hidden text-white text-2xl" on:click={() => isOpen = !isOpen}>
              {isOpen ? "✖" : "☰"}
          </button>
  
          <!-- Website Name (Centered) -->
          <div class="text-xl font-bold flex-1 text-center lg:text-left">
              <a href="/" class="hover:text-blue-500 underline">Understocks</a>
          </div>
  
          <!-- Right Menu (Desktop) -->
          <div class="hidden lg:flex space-x-6 text-lg font-medium">
              <a href="/" class="hover:text-blue-500">How it works</a>
              <a href="/" class="hover:text-blue-500">Contact</a>
          </div>
      </div>
  
      <!-- Mobile Menu (Dropdown) -->
      {#if isOpen}
      <div class="lg:hidden flex flex-col space-y-4 text-center bg-black py-4">
          <a href="/" class="hover:text-blue-500">How it works</a>
          <a href="/" class="hover:text-blue-500">Contact</a>
      </div>
      {/if}
  </nav>