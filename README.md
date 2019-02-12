#Stock Registry 
Distributed stock ticker system written in a variety of languages. Just a learning opportunity for myself

## API Spec

Every response will have the form 

```json
{
    "data":"Mixed type with content",
    "message": "Description of what happened"
}
```

Following response definitions will detail the values of the `data field`

### List all stocks

**Definition**

`GET /stocks

**Response**

- `200 OK

```json
[
    {
        "ticker": "NVDA",
        "stock": "NVIDIA",
        "index": "NASDAQ",
        "last-price": "150.49"
    },
    {
        "ticker": "AAPL",
        "stock": "APPLE INC",
        "index": "NASDAQ",
        "last-price": "170.89"
    }
]
```

### Registering a new stock

**Definition**

`POST /stocks`

**Arguments**

- `"ticker":string` the given ticker symbol
- `"stock":string` the company name
- `"index":string` the listed index for the company 
- `"last-price":string` the last given share price

If a stock with the given ticker exists already, the existing stock will be overwritten with the new one.

**Response**

- `201 Created` on success

```json
{
        "ticker": "AAPL",
        "stock": "APPLE INC",
        "index": "NASDAQ",
        "last-price": "170.89"
}
```

## Lookup stock details

`GET /stocks/<ticker>`

**Response**

- `404 Not Found` if the stock does not exist
- `200 OK` on success

```json
{
        "ticker": "AAPL",
        "stock": "APPLE INC",
        "index": "NASDAQ",
        "last-price": "170.89"
}
```

## Delete a stock

**Definition**

`DELETE /stocks/<ticker>`

**Response**

- `404 Not Found` if the stock does not exist
- `204 No Content` on success