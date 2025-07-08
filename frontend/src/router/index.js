import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../components/Dashboard.vue'
import DeviceDiscovery from '../components/DeviceDiscovery.vue'
import DetailedScan from '../components/DetailedScan.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/discovery', component: DeviceDiscovery },
  { path: '/detailed', component: DetailedScan },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router