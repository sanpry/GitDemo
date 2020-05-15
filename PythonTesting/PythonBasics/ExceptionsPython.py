try:
    with open('test.txt', 'r') as reader:
        reader.read()

except:  # Note: instead of catch, we have except.
    print("reached this block, only cause try block failed")

finally:  #executes even if try block passes or fails
    print("must execute; cleaning up the process")
