<template>
  <div class="app">
    <Sidebar />
    <div class="main-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
</script>

<style>
.app {
  display: flex;
}
.main-content {
  flex-grow: 1;
  padding: 1rem;
}
</style>
