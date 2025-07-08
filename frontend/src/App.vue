<template>
  <div class="flex h-screen">
    <Sidebar />
    <div class="flex-1 p-6 overflow-y-auto">
      <Dashboard />
    </div>
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
import Dashboard from './views/Dashboard.vue'
</script>
