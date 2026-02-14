## Exercise
Write a program that reads and writes blocks of data

## Reference Solution
```python
import os

class BlockDataRW:
    def __init__(self, block_size=1024):
        """
        Initialize the BlockDataRW class.

        Args:
            block_size (int): The size of each block in bytes. Defaults to 1024.
        """
        self.block_size = block_size

    def read_block(self, file_path, block_number):
        """
        Read a block of data from a file.

        Args:
            file_path (str): The path to the file.
            block_number (int): The number of the block to read.

        Returns:
            bytes: The block of data.
        """
        with open(file_path, 'rb') as file:
            file.seek(block_number * self.block_size)
            return file.read(self.block_size)

    def write_block(self, file_path, block_number, data):
        """
        Write a block of data to a file.

        Args:
            file_path (str): The path to the file.
            block_number (int): The number of the block to write.
            data (bytes): The block of data to write.
        """
        with open(file_path, 'r+b') as file:
            file.seek(block_number * self.block_size)
            file.write(data)

    def read_all_blocks(self, file_path):
        """
        Read all blocks of data from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            list: A list of all blocks of data.
        """
        blocks = []
        with open(file_path, 'rb') as file:
            while True:
                block = file.read(self.block_size)
                if not block:
                    break
                blocks.append(block)
        return blocks

    def write_all_blocks(self, file_path, blocks):
        """
        Write all blocks of data to a file.

        Args:
            file_path (str): The path to the file.
            blocks (list): A list of all blocks of data.
        """
        with open(file_path, 'wb') as file:
            for block in blocks:
                file.write(block)


def main():
    # Example usage:
    file_path = 'example.txt'
    block_data_rw = BlockDataRW()

    # Create a sample file
    with open(file_path, 'w') as file:
        for i in range(10):
            file.write(f'Block {i}\n' * 100)

    # Read a block of data
    block_number = 5
    block_data = block_data_rw.read_block(file_path, block_number)
    print(f'Block {block_number} data:')
    print(block_data.decode())

    # Write a block of data
    new_block_data = b'New block data'
    block_data_rw.write_block(file_path, block_number, new_block_data)

    # Read all blocks of data
    blocks = block_data_rw.read_all_blocks(file_path)
    print('\nAll blocks of data:')
    for i, block in enumerate(blocks):
        print(f'Block {i} data:')
        print(block.decode())

    # Write all blocks of data
    new_blocks = [b'New block 1', b'New block 2', b'New block 3']
    block_data_rw.write_all_blocks(file_path, new_blocks)

    # Read all blocks of data again
    blocks = block_data_rw.read_all_blocks(file_path)
    print('\nAll blocks of data after writing:')
    for i, block in enumerate(blocks):
        print(f'Block {i} data:')
        print(block.decode())


if __name__ == '__main__':
    main()
```

## Generated Output
```
Block 5 data:
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7


All blocks of data:
Block 0 data:
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 0
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1

Block 1 data:
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 1
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2

Block 2 data:
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 2
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3

Block 3 data:
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 3
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 4
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5

Block 4 data:
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 5
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6

Block 5 data:
New block data6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 6
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7

Block 6 data:
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 7
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8
Block 8

Block 7 data:
Block 8
Block 8
Block 8
Block 8
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9
Block 9


All blocks of data after writing:
Block 0 data:
New block 1New block 2New block 3
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
