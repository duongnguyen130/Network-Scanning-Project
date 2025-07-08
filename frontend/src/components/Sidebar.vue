<template>
  <div class="w-64 bg-[#0f1f3e] text-white h-screen flex flex-col">
    <div class="flex items-center gap-2 p-4 text-2xl font-bold">
      <img src="../assets/logo.png"  alt="Logo" class="w-6 h-6" />
      Network Scanning Admin
    </div>
    <nav class="flex flex-col gap-2 p-2">
      <RouterLink to="/" class="nav-item">
        <Lock class="w-5 h-5" />
        Dashboard
      </RouterLink>
      <RouterLink to="/device-discovery" class="nav-item">
        <Wifi class="w-5 h-5" />
        Hosts Discovery
      </RouterLink>
      <RouterLink to="/detailed-scan"  class="nav-item">
        <Search class="w-5 h-5" />
        Devices Discovery
      </RouterLink>
      <RouterLink to="/settings" class="nav-item">
        <Settings class="w-5 h-5" />
        Settings
      </RouterLink>
    </nav>
  </div>
</template>

<script setup>
// All icons are auto-registered via main.js
</script>

<style scoped>
.nav-item {
  @apply flex items-center gap-3 px-4 py-2 rounded hover:bg-[#1a2a4f] transition;
}
</style>
