<template>
  <div class="flex h-screen">
    <Sidebar />
    <div class="flex-1 bg-gray-50 p-6 overflow-auto">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
</script>