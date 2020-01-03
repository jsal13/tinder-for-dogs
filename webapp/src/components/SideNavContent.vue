<template>
    <div>
        VUE_APP_API_ADDRESS: <strong>{{ apiAddress }}</strong>
    </div>
</template>

<script>
export default {
    name: 'SideNavContent',
    data: () => ({
        apiAddress: process.env.VUE_APP_API_ADDRESS
    })
}
</script>