import axios from "axios"

axios.defaults.baseURL = process.env.VUE_APP_API_BASE


export interface Spot {
    id: number
    name: string
}

export async function createSpot(name: string): Promise<Spot> {
    const resp = await axios.request<Spot>({
        method: "post",
        url: "spot",
        data: {
            name
        }
    })
    return resp.data
}

export async function getSpot(id: number): Promise<Spot> {
    const resp = await axios.request<Spot>({
        method: "get",
        url: `spot/${id}`
    })
    return resp.data
}
